# EMA Hourly Continuation — XMR/USDT P8_50

**Symbol:** XMR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 622 |
| net_profit_factor | 0.6876 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9210 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -2.8863 |
| sortino_ratio | -1.0280 |
| max_drawdown | 0.6966 |
| cagr | -0.3757 |
| net_avg_win | 51.2316 |
| net_avg_loss | -68.5291 |
| avg_hold_time_bars | 11.9003 |
| exposure | 0.3365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
