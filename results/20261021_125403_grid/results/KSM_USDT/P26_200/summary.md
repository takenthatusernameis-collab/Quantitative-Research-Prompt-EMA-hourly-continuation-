# EMA Hourly Continuation — KSM/USDT P26_200

**Symbol:** KSM/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 278 |
| net_profit_factor | 0.8185 |
| net_win_rate | 0.5072 |
| gross_profit_factor | 1.0132 |
| gross_win_rate | 0.5072 |
| sharpe_ratio | -1.0273 |
| sortino_ratio | -0.2450 |
| max_drawdown | 0.3186 |
| cagr | -0.1079 |
| net_avg_win | 79.7192 |
| net_avg_loss | -100.2427 |
| avg_hold_time_bars | 46.5216 |
| exposure | 0.5879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
