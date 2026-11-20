# EMA Hourly Continuation — P2P/USDT P20_21

**Symbol:** P2P/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1122 |
| net_profit_factor | 0.1032 |
| net_win_rate | 0.2032 |
| gross_profit_factor | 0.3618 |
| gross_win_rate | 0.2246 |
| sharpe_ratio | -18.7082 |
| sortino_ratio | -9.4059 |
| max_drawdown | 1.0000 |
| cagr | -0.9946 |
| net_avg_win | 5.0467 |
| net_avg_loss | -12.4727 |
| avg_hold_time_bars | 2.4902 |
| exposure | 0.1270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
