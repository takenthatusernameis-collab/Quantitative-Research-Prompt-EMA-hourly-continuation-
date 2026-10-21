# EMA Hourly Continuation — WIF/USDT P21_34

**Symbol:** WIF/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 237 |
| net_profit_factor | 0.8176 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0376 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -1.0646 |
| sortino_ratio | -0.2352 |
| max_drawdown | 0.3523 |
| cagr | -0.1035 |
| net_avg_win | 89.6317 |
| net_avg_loss | -112.4385 |
| avg_hold_time_bars | 5.0211 |
| exposure | 0.0541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
