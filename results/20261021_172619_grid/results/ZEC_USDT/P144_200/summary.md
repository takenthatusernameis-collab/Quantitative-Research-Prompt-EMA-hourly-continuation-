# EMA Hourly Continuation — ZEC/USDT P144_200

**Symbol:** ZEC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 161 |
| net_profit_factor | 0.8638 |
| net_win_rate | 0.5280 |
| gross_profit_factor | 1.0991 |
| gross_win_rate | 0.5280 |
| sharpe_ratio | -0.5100 |
| sortino_ratio | -0.0934 |
| max_drawdown | 0.1573 |
| cagr | -0.0432 |
| net_avg_win | 78.3854 |
| net_avg_loss | -101.4902 |
| avg_hold_time_bars | 7.7329 |
| exposure | 0.0566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
