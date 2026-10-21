# EMA Hourly Continuation — XRP/USDT P20_34

**Symbol:** XRP/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.6740 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0849 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -1.9910 |
| sortino_ratio | -0.4470 |
| max_drawdown | 0.4179 |
| cagr | -0.1854 |
| net_avg_win | 66.5755 |
| net_avg_loss | -105.5237 |
| avg_hold_time_bars | 4.7934 |
| exposure | 0.0527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
