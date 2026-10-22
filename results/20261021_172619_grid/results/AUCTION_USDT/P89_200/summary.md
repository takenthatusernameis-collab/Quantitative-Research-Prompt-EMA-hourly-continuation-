# EMA Hourly Continuation — AUCTION/USDT P89_200

**Symbol:** AUCTION/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.5696 |
| net_win_rate | 0.4487 |
| gross_profit_factor | 0.8031 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -3.1822 |
| sortino_ratio | -0.7823 |
| max_drawdown | 0.6172 |
| cagr | -0.3152 |
| net_avg_win | 58.1472 |
| net_avg_loss | -83.0955 |
| avg_hold_time_bars | 15.9295 |
| exposure | 0.2249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
