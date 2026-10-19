# EMA Hourly Continuation — STX/USDT P12_144

**Symbol:** STX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.6330 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9025 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.9815 |
| sortino_ratio | -0.8766 |
| max_drawdown | 0.6981 |
| cagr | -0.3474 |
| net_avg_win | 53.3898 |
| net_avg_loss | -76.7712 |
| avg_hold_time_bars | 35.5973 |
| exposure | 0.7200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
