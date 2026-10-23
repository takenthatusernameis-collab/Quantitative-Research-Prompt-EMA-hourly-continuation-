# EMA Hourly Continuation — NYM/USDT P8_89

**Symbol:** NYM/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.4406 |
| net_win_rate | 0.3997 |
| gross_profit_factor | 0.7725 |
| gross_win_rate | 0.4191 |
| sharpe_ratio | -7.0793 |
| sortino_ratio | -2.4488 |
| max_drawdown | 0.9581 |
| cagr | -0.7129 |
| net_avg_win | 30.4971 |
| net_avg_loss | -46.0846 |
| avg_hold_time_bars | 24.3689 |
| exposure | 0.6845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
