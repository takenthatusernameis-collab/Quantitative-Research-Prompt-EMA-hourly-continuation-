# EMA Hourly Continuation — APE/USDT P8_34

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.6838 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.8915 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -3.6512 |
| sortino_ratio | -1.3781 |
| max_drawdown | 0.8141 |
| cagr | -0.4686 |
| net_avg_win | 53.4455 |
| net_avg_loss | -66.0517 |
| avg_hold_time_bars | 8.1280 |
| exposure | 0.2597 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
