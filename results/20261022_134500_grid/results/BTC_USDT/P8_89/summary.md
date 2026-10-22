# EMA Hourly Continuation — BTC/USDT P8_89

**Symbol:** BTC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.4501 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 0.9666 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -5.9906 |
| sortino_ratio | -2.1053 |
| max_drawdown | 0.9541 |
| cagr | -0.6594 |
| net_avg_win | 23.2310 |
| net_avg_loss | -44.5842 |
| avg_hold_time_bars | 22.8193 |
| exposure | 0.6618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
