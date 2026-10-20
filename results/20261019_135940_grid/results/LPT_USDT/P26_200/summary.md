# EMA Hourly Continuation — LPT/USDT P26_200

**Symbol:** LPT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.6732 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9047 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -2.6090 |
| sortino_ratio | -0.7805 |
| max_drawdown | 0.6408 |
| cagr | -0.3062 |
| net_avg_win | 57.8380 |
| net_avg_loss | -78.2331 |
| avg_hold_time_bars | 25.7773 |
| exposure | 0.5261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
