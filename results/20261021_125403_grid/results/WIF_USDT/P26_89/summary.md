# EMA Hourly Continuation — WIF/USDT P26_89

**Symbol:** WIF/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.9204 |
| net_win_rate | 0.5260 |
| gross_profit_factor | 1.0944 |
| gross_win_rate | 0.5260 |
| sharpe_ratio | -0.5053 |
| sortino_ratio | -0.1533 |
| max_drawdown | 0.3785 |
| cagr | -0.0734 |
| net_avg_win | 86.4685 |
| net_avg_loss | -104.2319 |
| avg_hold_time_bars | 14.1242 |
| exposure | 0.2844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
