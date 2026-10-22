# EMA Hourly Continuation — LUNC/USDT P89_144

**Symbol:** LUNC/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.4975 |
| net_win_rate | 0.4632 |
| gross_profit_factor | 0.9673 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -5.5060 |
| sortino_ratio | -1.8917 |
| max_drawdown | 0.9033 |
| cagr | -0.6005 |
| net_avg_win | 32.8886 |
| net_avg_loss | -57.0514 |
| avg_hold_time_bars | 4.7231 |
| exposure | 0.1256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
