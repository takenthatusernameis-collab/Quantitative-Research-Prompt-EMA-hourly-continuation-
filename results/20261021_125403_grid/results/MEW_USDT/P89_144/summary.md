# EMA Hourly Continuation — MEW/USDT P89_144

**Symbol:** MEW/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.7388 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9374 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -1.6584 |
| sortino_ratio | -0.4217 |
| max_drawdown | 0.4135 |
| cagr | -0.1760 |
| net_avg_win | 70.2779 |
| net_avg_loss | -91.0090 |
| avg_hold_time_bars | 7.8139 |
| exposure | 0.1126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
