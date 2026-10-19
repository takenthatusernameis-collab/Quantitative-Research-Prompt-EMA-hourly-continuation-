# EMA Hourly Continuation — HBAR/USDT P12_26

**Symbol:** HBAR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1455 |
| net_profit_factor | 0.3691 |
| net_win_rate | 0.4392 |
| gross_profit_factor | 0.8559 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -11.5260 |
| sortino_ratio | -6.2231 |
| max_drawdown | 0.9997 |
| cagr | -0.9585 |
| net_avg_win | 9.1514 |
| net_avg_loss | -19.4171 |
| avg_hold_time_bars | 2.6838 |
| exposure | 0.1775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
