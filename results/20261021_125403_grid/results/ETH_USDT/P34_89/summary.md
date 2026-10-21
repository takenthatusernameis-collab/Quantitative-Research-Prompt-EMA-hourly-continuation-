# EMA Hourly Continuation — ETH/USDT P34_89

**Symbol:** ETH/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.6255 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9356 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -2.6437 |
| sortino_ratio | -0.7235 |
| max_drawdown | 0.5831 |
| cagr | -0.2833 |
| net_avg_win | 52.8991 |
| net_avg_loss | -81.3821 |
| avg_hold_time_bars | 13.6548 |
| exposure | 0.2265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
