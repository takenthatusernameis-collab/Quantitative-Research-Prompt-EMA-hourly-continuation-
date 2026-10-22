# EMA Hourly Continuation — ZKJ/USDT P12_21

**Symbol:** ZKJ/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1618 |
| net_profit_factor | 0.1925 |
| net_win_rate | 0.2478 |
| gross_profit_factor | 0.5384 |
| gross_win_rate | 0.3449 |
| sharpe_ratio | -21.9300 |
| sortino_ratio | -13.3826 |
| max_drawdown | 1.0000 |
| cagr | -0.9994 |
| net_avg_win | 5.9466 |
| net_avg_loss | -10.1763 |
| avg_hold_time_bars | 2.8405 |
| exposure | 0.2089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
