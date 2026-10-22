# EMA Hourly Continuation — XDC/USDT P12_89

**Symbol:** XDC/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 887 |
| net_profit_factor | 0.3399 |
| net_win_rate | 0.4442 |
| gross_profit_factor | 0.8073 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -7.7105 |
| sortino_ratio | -3.1717 |
| max_drawdown | 0.9846 |
| cagr | -0.8093 |
| net_avg_win | 12.8629 |
| net_avg_loss | -30.2476 |
| avg_hold_time_bars | 11.3337 |
| exposure | 0.4570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
