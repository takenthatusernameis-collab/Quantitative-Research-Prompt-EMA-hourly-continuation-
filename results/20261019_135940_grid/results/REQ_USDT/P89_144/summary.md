# EMA Hourly Continuation — REQ/USDT P89_144

**Symbol:** REQ/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.3151 |
| net_win_rate | 0.3281 |
| gross_profit_factor | 0.7776 |
| gross_win_rate | 0.3689 |
| sharpe_ratio | -10.5704 |
| sortino_ratio | -3.8739 |
| max_drawdown | 0.9935 |
| cagr | -0.8641 |
| net_avg_win | 21.8632 |
| net_avg_loss | -33.8852 |
| avg_hold_time_bars | 5.2826 |
| exposure | 0.1530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
