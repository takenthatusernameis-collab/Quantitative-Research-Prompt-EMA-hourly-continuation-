# EMA Hourly Continuation — W/USDT P12_89

**Symbol:** W/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.8821 |
| net_win_rate | 0.5166 |
| gross_profit_factor | 1.0469 |
| gross_win_rate | 0.5166 |
| sharpe_ratio | -0.7446 |
| sortino_ratio | -0.2348 |
| max_drawdown | 0.3013 |
| cagr | -0.1067 |
| net_avg_win | 74.1250 |
| net_avg_loss | -89.8026 |
| avg_hold_time_bars | 24.8444 |
| exposure | 0.5443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
