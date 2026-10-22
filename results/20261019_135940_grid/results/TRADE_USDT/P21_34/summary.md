# EMA Hourly Continuation — TRADE/USDT P21_34

**Symbol:** TRADE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 895 |
| net_profit_factor | 0.3470 |
| net_win_rate | 0.3709 |
| gross_profit_factor | 0.6812 |
| gross_win_rate | 0.3866 |
| sharpe_ratio | -10.1753 |
| sortino_ratio | -4.3323 |
| max_drawdown | 0.9962 |
| cagr | -0.8894 |
| net_avg_win | 15.9440 |
| net_avg_loss | -27.0937 |
| avg_hold_time_bars | 3.4302 |
| exposure | 0.1395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
