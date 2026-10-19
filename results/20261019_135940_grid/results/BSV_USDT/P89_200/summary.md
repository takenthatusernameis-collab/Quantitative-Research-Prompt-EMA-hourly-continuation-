# EMA Hourly Continuation — BSV/USDT P89_200

**Symbol:** BSV/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.4433 |
| net_win_rate | 0.3905 |
| gross_profit_factor | 0.7318 |
| gross_win_rate | 0.4063 |
| sharpe_ratio | -5.7676 |
| sortino_ratio | -1.7099 |
| max_drawdown | 0.8774 |
| cagr | -0.5664 |
| net_avg_win | 40.3879 |
| net_avg_loss | -58.3727 |
| avg_hold_time_bars | 10.5666 |
| exposure | 0.2128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
