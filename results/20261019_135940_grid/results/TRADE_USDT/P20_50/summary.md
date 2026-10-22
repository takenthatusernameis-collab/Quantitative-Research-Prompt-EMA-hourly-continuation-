# EMA Hourly Continuation — TRADE/USDT P20_50

**Symbol:** TRADE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 783 |
| net_profit_factor | 0.5314 |
| net_win_rate | 0.4342 |
| gross_profit_factor | 0.8546 |
| gross_win_rate | 0.4393 |
| sharpe_ratio | -6.3721 |
| sortino_ratio | -2.4883 |
| max_drawdown | 0.9581 |
| cagr | -0.7121 |
| net_avg_win | 31.8975 |
| net_avg_loss | -46.0649 |
| avg_hold_time_bars | 6.2618 |
| exposure | 0.2229 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
