# EMA Hourly Continuation — ETHFI/USDT P12_89

**Symbol:** ETHFI/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.7849 |
| net_win_rate | 0.4790 |
| gross_profit_factor | 0.9148 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -1.6866 |
| sortino_ratio | -0.5376 |
| max_drawdown | 0.4808 |
| cagr | -0.2208 |
| net_avg_win | 70.8017 |
| net_avg_loss | -82.9456 |
| avg_hold_time_bars | 22.6826 |
| exposure | 0.5165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
