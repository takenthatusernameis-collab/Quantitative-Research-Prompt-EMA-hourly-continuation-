# EMA Hourly Continuation — MTL/USDT P12_34

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1202 |
| net_profit_factor | 0.4725 |
| net_win_rate | 0.4210 |
| gross_profit_factor | 0.9396 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -9.8383 |
| sortino_ratio | -4.8115 |
| max_drawdown | 0.9977 |
| cagr | -0.9083 |
| net_avg_win | 17.6589 |
| net_avg_loss | -27.1714 |
| avg_hold_time_bars | 5.4268 |
| exposure | 0.2952 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
