# EMA Hourly Continuation — APE/USDT P8_21

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1638 |
| net_profit_factor | 0.3268 |
| net_win_rate | 0.4194 |
| gross_profit_factor | 0.7701 |
| gross_win_rate | 0.4402 |
| sharpe_ratio | -11.9858 |
| sortino_ratio | -6.8555 |
| max_drawdown | 0.9998 |
| cagr | -0.9672 |
| net_avg_win | 7.0663 |
| net_avg_loss | -15.6179 |
| avg_hold_time_bars | 2.8480 |
| exposure | 0.2120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
